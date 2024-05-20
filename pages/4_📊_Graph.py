import streamlit as st
import pandas as pd
import ssl
import matplotlib.pyplot as plt
import textwrap

# Set up page appearance
page_title = "Graph"
st.set_page_config(page_title, '💻', 'wide', 'collapsed')

# Project 4
st.markdown("### Project 4: Make a graph")
st.markdown("**Project description:** Here is the description of the project.")
st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
# st.markdown("**See the project in action**")
st.link_button(":blue[See code]", "https://github.com/beck1888/Streamlit-Graph-Projects")
st.divider()
if st.button("▶️ Run project", key='4', use_container_width=True):
    with st.status("Creating graph", expanded=True):
            st.write("🌐 Getting data from URL")

            # Set up certificate
            ssl._create_default_https_context = ssl._create_stdlib_context
            # Load the dataset
            url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-12-11/nyc_restaurants.csv'
            df = pd.read_csv(url)

            st.write("🧮 Processing data with pandas")

            # Set up dataframe
            df['cuisine_description'] = df['cuisine_description']
            # Make sure 'score' and 'cuisine_description' are not null
            df.dropna(subset=['score', 'cuisine_description'], inplace=True)

            # Calculate average scores using for loops
            score_sums = {}
            count = {}

            # Iterate through the DataFrame
            for index, row in df.iterrows():
                cuisine = row['cuisine_description']
                score = row['score']

                if cuisine in score_sums:
                    score_sums[cuisine] += score
                    count[cuisine] += 1
                else:
                    score_sums[cuisine] = score
                    count[cuisine] = 1

            # Calculate averages and store them in a dictionary
            average_scores = {cuisine: score_sums[cuisine] / count[cuisine] for cuisine in score_sums}

            # Make a formatted (accent free dictionary and rounded numbers)
            final_data = {}
            for key in average_scores.keys():
                key_new = key.replace("CafÃ©", "Cafe") # .replace("\u00c3\u00a9", "e").replace("é", "e")
                final_data[key_new] = round(average_scores[key])

            # Because a lower score is better, sort by low to high scores based on values
            def get_value(item):
                return item[1]

            # Sorting the dictionary items by value
            sorted_items = sorted(final_data.items(), key=get_value)

            # Creating a new dictionary with sorted items
            sorted_data = {}
            for key, value in sorted_items:
                sorted_data[key] = value

            st.write("📈 Plotting main curve")

            # Graph the data
            # Extracting data into lists to be read for plotting
            x = list(sorted_data.keys())
            y = list(sorted_data.values())

            # Define the colors based on values
            colors = []
            for value in y:
                if value < 15:
                    colors.append('green')  # Bars representing values less than 10 will be green
                elif 15 <= value <= 20:
                    colors.append('orange')  # Bars representing values between 10 and 20 will be yellow
                else:
                    colors.append('red')  # Bars representing values greater than 20 will be red


            def format_labels(labels, width):
                """Trim long labels based on content and wrap them to the specified width."""
                trimmed_labels = []
                for label in labels:
                    # Trim labels based on their content
                    if "Latin" in label:
                        label = "Latin"
                    elif "Bottled" in label:
                        label = "Drinks"
                    elif "Vietnamese" in label:
                        label = "Vietnamese"
                    
                    # Append the trimmed and wrapped label to the list
                    trimmed_labels.append(textwrap.fill(label, width))
            
                return trimmed_labels


            fig, ax = plt.subplots(figsize=(10, 8))  # Adjust the size as needed
            ax.barh(x, y, color=colors, height=0.8)
            ax.set_title('Average Health Code Violations Of Each Cuisine in NYC', fontsize=14)
            ax.set_xlabel('Amount of violations', fontsize=12)
            ax.set_ylabel('Type of restaurant', fontsize=12)
            ax.set_yticks(range(len(x)))
            ax.set_yticklabels(format_labels(x, width=50), fontsize=5)
            plt.tight_layout()
            st.write("✅ Done")

    # Display the plot
    st.pyplot(fig)  # Pass the figure to st.pyplot() function
    st.balloons()