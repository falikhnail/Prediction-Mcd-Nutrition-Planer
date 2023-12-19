# Nutrition_Planner-tool-using-data-analysis-and-python
URL for the App: https://mcdnutritionplanner.streamlit.app

## Description
This Streamlit web application is a nutrition planner designed to assist users in planning a nutritionally balanced meal at McDonald's. This tool takes user input for various nutrition constraints, filters McDonald's menu items based on these constraints, and recommends a set of menu items that best match the user's preferences.

## Key Features
- **Nutrition Constraints:** Users can set constraints for total fat, saturated fat, sugar, carbohydrates, and protein.
- **Recommendations:** The application filters McDonald's menu items based on user input and recommends a list of menu items that meet the specified nutrition constraints.
- **Visualization:** The recommended menu is visualized through a table and a bar plot displaying the nutrition information of the selected items.

## Technologies Used
- Python
- Streamlit for the user interface
- Matplotlib.pyplot for visualizations
- Seaborn for statistical data visualization
- Pandas for data manipulation

## How to Use
1. Clone or download this repository to your local machine.
2. Install the required dependencies using the following command: pip install streamlit pandas matplotlib seaborn
3. Download the menu data file `Menu.csv.csv` and place it in the project directory.
4. Run the Streamlit app using the following command:streamlit run Analyzer.py
5. Adjust the sliders in the sidebar to set your preferred nutrition constraints
7. The results will be displayed on the screen, including a bar plot.

## Contributing
- Feel free to explore and contribute to the project! Your feedback and contributions are highly appreciated.

## Acknowledgments
- Inspiration for this project was drawn from [Kyle Pastor's article](https://towardsdatascience.com/making-mcdonalds-healthy-197f537f931d) and [Avery Smith](https://www.youtube.com/watch?v=3bbFc1225-4&list=PLo0oTKi2fPNiMBo2hXreEetXCXev170ZZ&index=29).


