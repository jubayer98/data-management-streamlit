import streamlit as st
import pandas as pd
from io import StringIO

def main():
    st.title("UKD - SAMPLE INFORMATION")

    uploaded_file = st.file_uploader("UPLOAD THE SAMPLE REPORT FILE (.txt format only)", type="txt")

    if uploaded_file is not None:
        try:
            # Read the uploaded file
            file_contents = uploaded_file.getvalue().decode("utf-8")

            # Convert the text to DataFrame
            df = pd.read_csv(StringIO(file_contents), delimiter="#")

            # Filter based on 'denevo' column
            filter_option = st.radio("Denovo Status:", ('All', 'Yes', 'No'))

            if filter_option == 'Yes':
                filtered_df = df[df['denovo'] == 'Yes']
            elif filter_option == 'No':
                filtered_df = df[df['denovo'] == 'No']
            else:
                filtered_df = df

            # Display the DataFrame
            st.write("Filtered DataFrame:", filtered_df)

            # Show total number of rows
            st.write("Total number of rows:", len(filtered_df))

            # Download option
            if st.button('Create Filtered Data File (.txt Format Only)'):
                # Convert DataFrame to # separated text
                csv_data = filtered_df.to_csv(sep='#', index=False)
                # Offer the file as a download
                st.download_button(label="Download Now", data=csv_data, file_name='filtered_data.txt', mime='text/plain')

        except Exception as e:
            st.error("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()