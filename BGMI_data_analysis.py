"""
BGMI Player Performance Analysis
Author: Sahil Kole
Description:
This project analyzes player performance using Python and Pandas.
It calculates K/D ratio, win percentage, survival time,
and compares performance across different modes.

"""

import numpy as np 
import pandas as pd

data = pd.read_csv("bgmi_medium_level_dataset_100_rows (1).csv", encoding = "Latin1")

#PHASE 01

print("TOP 5 ROWS: \n",data.head(5))                                            # TOP 5 ROWS
print("NUMBER OR ROWS AND COL ARE: \n",data.shape)                              # NUMBER OF ROWS AND COLUMN
print("DATA INFORMATION: \n",data.info)                                         # INFORMATION OF DATA
print("NUMBER OF NULL VALUES: \n",data.isnull().sum())                          # NUMBER OF NULL VALUES

#PHASE 02

total_kills = data.groupby("Player")["Kills"].sum()                             # TOTAL KILLS PER PLAYER
print("TOTAL KILLS ARE : \n",total_kills)
total_mat = data.groupby("Player")["Match_No"].count()                          # TOTAL MATCHES PER PLAYER
print("TOTAL MATCHES ARE : \n ",total_mat)

kd = total_kills/total_mat                                                      # KILL/DEATH RATIO
print("KD RATIO IS :  \n ",kd)
                                                                     



total_wins = data.groupby("Player")["Wins"].sum()                             # TOTAL WINS PER PLAYER
print("TOTAL WINS PER PLAYER: \n",total_wins)

win_percent = total_wins/total_mat                                            # WIN PERCENTAGE PER PLAYER
print("WIN PERCENTAGE IS : \n ",win_percent)


#PHASE 03

total_kills.sort_values( ascending=[False],inplace = True)                    # SORTED TOTAL KILLS PER PLAYER IN DESCENDING ORDER
print("TOTAL KILLS IN DESCENDING ORDER: \n",total_kills)                         

top5 = total_kills.head(5)                                                    # TOP 5 PLAYERS WITH HIGHEST KILLS
print("TOP 5 PLAYERS ARE : \n", top5)      



total_dam = data.groupby("Player")["Damage"].sum()                            # TOTAL DAMAGE PER PLAYER
print("TOTAL DAMAGE PER PLAYER IS: \n", total_dam)

total_dam.sort_values(ascending=False, inplace = True)                        # TOTAL DAMAGE PER PLAYER SORTED IN DESCENDING ORDER
print("TOTAL DAMAGE PER PLAYER IN DESCENDING ORDER : \n",total_dam)

high_dam = total_dam.head(1)                                                  # PLAYER WITH HIGHEST DAMAGE
print("PLAYER WITH HIGHEST DAMAGE: \n", high_dam)




kd.sort_values(ascending = False, inplace = True)                             # SORTED K/D RATIO PER PLAYER IN DESCENDING ORDER
print("KD RATIO PER PLAYER IN DESCENDING ORDER: \n", kd)                                

high_kd = kd.head(1)                                                          # PLAYER WITH HIGHEST K/D RATIO
print("PLAYER WITH HIGHEST KD RATIO IS : \n",high_kd)




win_percent.sort_values(ascending = False, inplace = True)                    # WIN PERCENTAGE PER PLAYER IN DESCENDING ORDER
print("WIN PERCENTAGE PER PALYER IN DESCENDING ORDER : \n",win_percent)

high_win_rate = win_percent.head(1)                                           # PLAYER WITH HIGHEST WIN PERCENTAGE
print("PLAYER WITH HIGHEST WIN RATE: \n",high_win_rate)



total_sur = data.groupby("Player")["Survival_Time_Minutes"].sum()             # TOTAL SURVIVAL TIME PER PLAYER
print("TOTAL SURVIVAL TIME PER PLAYER: \n",total_sur) 
 
total_sur.sort_values(ascending=False, inplace=True)                          # TOTAL SURVIVAL TIME PER PLAYER IN DESCENDING ORDER
print("TOTAL SURVIVAL TIME IN DESCENDING ORDER: \n",total_sur)

consistent = total_sur.head(1)                                                # MOST CONSISTENT PLAYER
print(consistent)

# PHASE 04

moding = data.groupby("Mode")["Kills"].sum()                                  # TOTAL KILLS PER MODE
print("TOTAL KILLS IN EACH MODE: ",moding)

total_mode_mat = data.groupby("Mode")["Match_No"].count()                     # TOTAL MATCHES PER MODE
print("TOTAL MATCHES PER MODE: \n",total_mode_mat)

average_kills = moding / total_mode_mat                                       # AVERAGE KILLS PER MODE
print("AVERAGE KILLS PER MODE: \n",average_kills)

average_kills.sort_values(ascending = False, inplace = True)                  # AVERAGE KILLS PER MODE IN DESCENDING ORDER
print("AVERAGE KILLS IN DESCENDING ORDER: \n",average_kills)

high_avg_kills = average_kills.head(1)                                        # HIGHEST AVERAGE KILLS IN MODE
print("MODE WITH HIGHEST AVERAGE KILLS: \n",high_avg_kills)




total_wins = data.groupby("Mode")["Wins"].sum()                               # TOTAL WINS PER MODE
print("TOTAL WINS PER MODE: \n",total_wins)

win_rate = total_wins / total_mode_mat                                        # WIN RATE PER MODE
print("WIN RATE PER MODE: \n ", win_rate )

win_rate.sort_values(ascending = False, inplace = True)                       # WIN RATE PER MODE IN DESCENDING ORDER
print("WIN RATE IN DESCENDING ORDER: \n", win_rate)

high_win_rate = win_rate.head(1)                                              # HIGHEST WIN RATE IN MODE
print("HIGHEST WIN RATE IN MODE",high_win_rate)



total_sur = data.groupby("Mode")["Survival_Time_Minutes"].sum()               # TOTAL SURVIVAL TIME PER MODE
print("TOTAL SURVIVAL TIME PER MODE: \n",total_sur)

total_sur.sort_values(ascending=False, inplace=True)                          # TOTAL SURVIVAL TIME IN DESCENDING ORDER
print("TOTAL SURVIVAL TIME IN DESCENDING ORDER: \n",total_sur)

high_sur = total_sur.head(1)                                                  # HIGHEST SURVIVAL TIME IN MODE
print("HIGHEST SURVIVAL TIME IN MODE: \n",high_sur)          

#PHASE 05

data.drop(columns = ["Mode", "Player"], inplace = True)                      # COLUMNS MODE AND PLAYER DROPPED
print(data)

print("CORRELATION BETWEEN COLUMNS: \n",data.corr())                         # CORRELATION BETWEEN COLUMNS






























