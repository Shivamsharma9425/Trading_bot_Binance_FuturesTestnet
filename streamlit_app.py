import streamlit as st  # type: ignore
from bot.orders import place_order
from bot.validators import *

st.title("Binance Futures Testnet Trading Bot")
st.write("Simple UI to place Market or Limit orders")
symbol = st.text_input("Symbol", "BTCUSDT")

side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)
order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)
quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.01
)

price = None

if order_type == "LIMIT":
    price = st.number_input(
        "Price",
        min_value=0.0,
        value=60000.0
    )
if st.button("Place Order"):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        st.subheader("Order Summary")
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Symbol:**", symbol)
            st.write("**Side:**", side)
        with col2:
            st.write("**Order Type:**", order_type)
            st.write("**Quantity:**", quantity)

        if price:
            st.write("**Price:**", price)

        with st.spinner("Placing order on Binance Testnet..."):
            order = place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

        st.success("Order Successful")
        st.subheader("Order Response")
        st.write("**Order ID:**", order.get("orderId"))
        st.write("**Status:**", order.get("status"))
        st.write("**Executed Quantity:**", order.get("executedQty"))

    except Exception as e:

        st.error(f"Order Failed: {str(e)}")