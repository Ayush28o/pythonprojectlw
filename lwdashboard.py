import streamlit as st
import pandas as pd

def main():
    """Main function to run the Streamlit application for Laundry Service."""
    st.set_page_config(page_title=" Laundry Wallah Service", layout="centered")

    st.title("Welcome to Laundry Service")
    
    st.markdown("""Welcome to Laundry Wallah, your local source for clean, convenient laundry services in Jaipur. We offer a bright, modern space with state-of-the-art self-service machines and free Wi-Fi. For the ultimate time-saver, try our reliable Wash & Fold and pickup/delivery options. Our mission is simple: to provide exceptional quality and friendly service so you can skip the chore. Stop by today and experience the difference!""")

    st.header("Our Services")
    
   
    st.selectbox("Choose a service:", ["Self-Service Laundry", "Wash & Fold", "Pickup & Delivery"])
    
    
    if st.button("Schedule Now"):
        st.success("Your laundry service has been scheduled!")
        
    file = st.file_uploader("Upload your laundry list:", type=["txt", "pdf"])
    if file:
        content = file.read()
        st.write("File uploaded successfully!")
        st.text(content.decode("utf-8") if isinstance(content, bytes) else content) # Decode content if it's bytes

    st.header("Service Costs")

    # Data for the services table
    data = {"Service": ["Self-Service Laundry", "Wash & Fold", "Pickup & Delivery"], "Cost (per kg)": ["₹20", "₹30", "₹50"]}
    df = pd.DataFrame(data)
    
    # Display the table
    st.table(df)
    
    st.header("Contact Us")
    st.text("Email: laundrywallah@gmail.com")
    st.write("Thank you for choosing Laundry Wallah!")

    
    if st.button("Book Now"):
        st.success("Booking confirmed! We look forward to serving you.")

if __name__ == "__main__":
    main()