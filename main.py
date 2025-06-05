

import streamlit as st

# Define Coffee class
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Initialize Order in Session State
if "order" not in st.session_state:
    st.session_state.order = []

def add_item(coffee):
    st.session_state.order.append(coffee)
    st.success(f"☕ Added {coffee.name} to your order!")

def show_order():
    if not st.session_state.order:
        st.warning("🚫 No items in order.")
        return
    st.subheader("🛒 Your Order")
    for i, item in enumerate(st.session_state.order, 1):
        st.write(f"{i}. {item.name} - ${item.price}")
    total = sum(item.price for item in st.session_state.order)
    st.write(f"💰 **Total: ${total}**")

def checkout():
    if not st.session_state.order:
        st.warning("❌ Your cart is empty.")
        return
    show_order()
    if st.button("✅ Proceed to Checkout"):
        st.success("🎉 Order Confirmed! Thank You!")
        st.session_state.order.clear()

# Main function
def main():
    st.markdown("<h1 style='color:orange'>☕ Coffee Shop App</h1>", unsafe_allow_html=True)
    
    # Create columns for side-by-side layout
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h2 style='color:purple'>📜 Menu</h2>", unsafe_allow_html=True)

        # Menu Items
        menu = [
            Coffee("Espresso", 2.50),
            Coffee("Latte", 3.00),
            Coffee("Cappuccino", 4.50),
            Coffee("Americano", 2.00),
        ]

        # Display Menu
        for coffee in menu:
            if st.button(f"{coffee.name} - ${coffee.price}"):
                add_item(coffee)

    with col2:
        st.markdown("<h2 style='color:blue'> 📦 Order Details</h2>", unsafe_allow_html=True)
        if st.button("🔎 View Order"):
            show_order()

        st.markdown("<h2 style='color:green'>💳 Checkout</h2>", unsafe_allow_html=True)
        if st.button("🛍️ Checkout"):
            checkout()

    # Footer
    st.markdown("---")
    st.markdown("👨‍💻 *Made by Muhammad Tariq Mahboob*")

# Run the app
if __name__ == "__main__":
    main()