This project uses Python to analyze and visualize data from the UK Premier League 2020/2021 season. The goal is to calculate and plot the total number of goals scored by each team (home and away) using Matplotlib and Seaborn.

---

## 📊 Features

* Fetches official match data from [football-data.co.uk](https://www.football-data.co.uk)
* Cleans and processes relevant goal data
* Aggregates home and away goals per team
* Visualizes total goals with a horizontal bar plot

---

## 🔧 Technologies Used

* Python
* pandas
* matplotlib
* seaborn
* requests
* io

---

## 🛠 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/premier-league-goals-visualization.git
   cd premier-league-goals-visualization
   ```

2. **Install dependencies**
   *(Make sure you have Python 3 installed)*

   ```bash
   pip install pandas matplotlib seaborn requests
   ```

3. **Run the script**

   ```bash
   python main.py
   ```

4. **Output**
   A bar plot showing total goals scored by each Premier League team during the 2020/2021 season will be displayed.

---

## 📁 Dataset

Data Source: [https://www.football-data.co.uk/mmz4281/2021/E0.csv](https://www.football-data.co.uk/mmz4281/2021/E0.csv)
Columns Used:

* `HomeTeam`
* `AwayTeam`
* `FTHG` (Full Time Home Goals)
* `FTAG` (Full Time Away Goals)

---

## 📌 Example Plot

![Example Plot](assets/total_goals_plot.png) <!-- optional if you want to include a saved image -->

---

## 📄 License

