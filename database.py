import pandas as pd

    
def save(gender,age,visit_count,transport,congestion,satisfaction,sculpture):
    idx = len(pd.read_csv("./database.csv"))
    new_df = pd.DataFrame({"gender":gender,
                           "age":age,
                           "visit_count":visit_count,
                            "transport":transport ,
                           "congestion":congestion,
                          "satisfaction" :satisfaction,
                          "sculpture":sculpture}, 
                         index = [idx])
    new_df.to_csv("./database.csv",mode = "a", header = False)
    return None

def savegwan(gender,age,visit_count,transport,congestion,satisfaction,sculpture):
    idx = len(pd.read_csv("./database.csv"))
    new_df = pd.DataFrame({"gender":gender,
                           "age":age,
                           "visit_count":visit_count,
                            "transport":transport ,
                           "congestion":congestion,
                          "satisfaction" :satisfaction,
                          "sculpture":sculpture}, 
                         index = [idx])
    new_df.to_csv("./databasegwan.csv",mode = "a", header = False)
    return None


def load_list():
    survey_list = []
    df = pd.read_csv("./house.csv")
    for i in range(len(df)):
        survey_list.append(df.iloc[i].tolist())
    return survey_list

def loadgwan_list():
    surveygwan_list = []
    df = pd.read_csv("./housegwan.csv")
    for i in range(len(df)):
        surveygwan_list.append(df.iloc[i].tolist())
    return surveygwan_list


def now_index():
    df = pd.read_csv("./database.csv")
    return len(df)-1


def load_survey(idx):
    df = pd.read_csv("./database.csv")
    survey_info = df.iloc[idx]
    return survey_info

def load_house(idx):
    df = pd.read_csv("house.csv")
    house_info = df.iloc[idx]
    return  house_info

def load_housegwan(idx):
    df = pd.read_csv("housegwan.csv")
    housegwan_info = df.iloc[idx]
    return housegwan_info


if __name__ =="__main__":
    load_list()
