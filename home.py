import streamlit as st

def main():
    # Add CSS styles to change the background color
    st.markdown(
        """
        <style>
        body {
            background-color: #000235;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image('./GSF/Ellipse_2.png', width=20)
    st.image('Other_19.png',width=20)
    st.image('Ellipse.png', width=20)

    st.write('# Explore Projection of Future Price and Sales')
    st.write('This sales forecasting website helps in giving a clear view of sales data')
    st.write('It provides statistical analysis data')

    if st.button('Get Started'):
        st.write('Redirecting to Sales page...')

if __name__ == '__main__':
    main()
