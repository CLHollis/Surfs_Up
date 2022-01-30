<image src="images/title_image_with_programs.PNG" width="900" height="500">[^1] [^2]

# Background of the Analysis:
Investing in Waves and Ice Cream: Open a surf & shake shop. Need investor backing. W.Wavy wants to invest but is concerned about the weather. Run some data analytics first to make sure the weather makes it a viable business worth investing in.
  
Data Source: hawaii.sqlite
Software: Python 3.9.7, Jupyter Notebook 6.4.6, Flask 1.1.2, SQLite3 3.36.0

### Task 1
W. Avy is concerned about the amount of precipitation on Oahu. There needs to be enough rain to keep everything green, but not so much that you lose out on that ideal surfing and ice cream weather. Conduct a Precipitation Analysis.
### Task 2
How many stations are being used to collect this information? Is it possible that we don't have enough data collection stations for this information to be valid?" Conduct a Weather Station Analysis.

[climate_analysis.ipynb](climate_analysis.ipynb)

### Task 3
The board of directors probably doesn't really care about the mechanics of the code you've written. They just want to be able to access the results. Use Flask, which will display the results in a webpage.

[app.py](app.py)

<image src="images/flask_welcome.PNG" width="350" height="200">
  
<image src="images/flask_precipitation.PNG" width="600" height="225">
  
<image src="images/flask_stations.PNG" width="500" height="150">
  
<image src="images/flask_temp_observations.PNG" width="400" height="150">

<image src="images/flask_min-avg-max_temps_June-2017.PNG" width="400" height="120">

# CHALLENGE PURPOSE
W. Avy likes your analysis, but he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

Determine the Summary Statistics for June, then December:
In SurfsUp_Challenge.ipynb use Python, Pandas functions and methods, and SQLAlchemy, retrieve all the temperatures for the month of June in the hawaii.sqlite database, by filtering the date column of the Measurements tableThen convert those temperatures to a list, create a DataFrame from the list, and generate the summary statistics. Repeate for the month of December.

      # importdependencies
      import numpy as np
      import pandas as pd
      import sqlalchemy
      from sqlalchemy.ext.automap import automap_base
      from sqlalchemy.orm import Session
      from sqlalchemy import create_engine, func

      # connect sqlite
      engine = create_engine("sqlite:///hawaii.sqlite")
      Base = automap_base()
      Base.prepare(engine, reflect=True)
      Measurement = Base.classes.measurement
      Station = Base.classes.station
      session = Session(engine)

      # find June temp stats
      june_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==6).all()
      june_temps_df = pd.DataFrame(june_temps, columns=['date','June Temps'])
      june_temps_df.describe()

      # find Dec temp stats
      dec_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==12).all()
      dec_temp_df = pd.DataFrame(dec_temps, columns=['date','December Temps'])
      dec_temp_df.describe()

# RESULTS
3 key differences in weather between June and December:
  - In my opinion, the minimum shows sales could slow around December because it may be a little too chilly to drink a milkshake outdoors.
  - There are more temp stats pulled in June than in December, which is unusual because there are more days in December, so more time to pull more temps. 
  - The average is about the same, so the "mood" for surfing and craving shakes should not differ too much throughout the year. Maybe a small sitting area with an cover for rainy weather would keep this shop poppin "rain or shine!"
<image src="images/summary_stats_comparison.PNG" width="350" height="400"> 

# SUMMARY
Two recommendations for further analysis:
  - Run profitability stats for shop "comps" on the other islands and Oahu.
  - Run precipitation for time of day to see when the operating hours to be open should be for the sunniest weather.

[^1]: [Surfboard Photo by Dick Brewer Surfboards](https://www.brewersurfboards.com/history). Accessed Jan. 29, 2022.
[^2]: [Feel Good Pineapple Smoothie Photo by Gimme Some Oven](https://www.gimmesomeoven.com/feel-good-pineapple-smoothie-recipe/). Accessed Jan. 29, 2022.
