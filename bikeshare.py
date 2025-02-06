import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    This will need to handle all case type of city name
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago', 'new york city', 'washington']  # Predefined list of valid strings
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    
    while True:
        city = input("Which city are you interested in? chicago, new york city, washington\n").lower()
        
        # Check if the input is in the list of valid strings
        if city not in valid_cities:
            print("Error: Invalid input. Please enter a valid city from the list.")
            continue
        else:
            break
                          
    # TO DO: get user input for month (all, january, february, ... , june
    while True:
        month = input("Which month? january, february, march, april, may, june, all\n").lower()
        if month not in valid_months:
            print("Error: Invalid input. Please enter a valid month from the list.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday 
    while True:
        day = input("Which day of the week? monday, tuesday, wednesday, thursday, friday, saturday, sunday, all\n").lower()
        if day not in valid_days:
            print("Error: Invalid input. Please enter a valid month from the list.")
            continue
        else:
            break
    print('-'*40)
    return city, month, day

    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze - keep 3 words for new york city
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    ## find the most popular hour
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)
    
    # TO DO: display the most common start hour
    ## convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    ## extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    ## find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)
    
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_Station_End_Station'] = df['Start Station'] + ' to ' + df['End Station']
    popular_start_end = df['Start_Station_End_Station'].mode()[0]
    print('Most Popular Start End Station Combination:', popular_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'] = pd.to_numeric(df['Trip Duration'], errors='coerce').fillna(0)
    total_travel_time = df['Trip Duration'].sum()
    print('The total trip duration is: ' + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average trip duration is: ' + str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)

    try:
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)


        # TO DO: Display earliest, most recent, and most common year of birth
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()

        print('The most common birth year is ' + str(most_common_year_of_birth))
        print('The earliest birth year is ' + str(earliest_year_of_birth))
        print('The most recent birth year is ' + str(most_recent_year_of_birth))
    except KeyError:
        print('No gender/birth data for Washington.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data_rows(df):
    """Ask user to see five rows of data (yes or no)
    print 5 rows of data for yes
    loop back and let them pick 5 more rows"""
    r = 0
    while True:
        raw = input("Show five rows of raw data? Yes or No\n").lower()
        if raw == 'yes':
            print(df[r:r+5])
            r = r+5
        else:
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break            

if __name__ == "__main__":
    main()
