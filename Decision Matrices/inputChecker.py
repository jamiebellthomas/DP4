import pandas as pd
#TODO
#Check:
#parent criteria at the top of the hierarchy match parent critaria one-to-one (DONE)
#criteria and sub-criteria are unique (no duplicates over any of the tiers) (DONE)
#critera and sub-criteria are in sequential order (no gaps) 
#no missing importance values
#informative error messages clearly highlighting the problem
# Load in data
data = pd.read_excel('hierarchy.xlsx', sheet_name='Sheet1', header=0)
def criteria_info(data):
    criteria_row = list(data.iloc[1])
    parent_criteria = [x for x in criteria_row if str(x) != 'nan']
    parent_criteria = parent_criteria[1:]
    return parent_criteria,len(parent_criteria)

def criteria_unique(parent_criteria:list):
    """
    Check that the criteria are unique (no duplicates on the top tier)
    """
    if len(parent_criteria) == len(set(parent_criteria)):
        return True
    else:
        return False

def parent_match(data,parent_criteria:list ,criteria_number:int):
    """
    Check that the parent criteria defined at the top of the input spreadsheet
    match the parent criteria defined in the spreadsheet and are only defined once
    """
    parent_in_data_list = []
    for i in range(0,criteria_number):
        parent_in_data = list(data.iloc[12+(21*(i))])
        parent = [x for x in parent_in_data if str(x) != 'nan']
        parent_in_data_list.append(parent[-1])
    if sorted(parent_criteria) == sorted(parent_in_data_list):
        return True
    else:
        return False


def sub_criteria_unique(data,criteria_number:int):
    """
    Check that the sub-criteria are unique (no duplicates over any of the tiers)
    """
    criteria_list = []
    for i in range(0,criteria_number):
        criteria = list(data.iloc[13+(21*(i))])
        criteria = [x for x in criteria if str(x) != 'nan']
        for j in range(0,len(criteria)):
            criteria_list.append(criteria[j])
    if len(criteria_list) == len(set(criteria_list)):
        return True
    else:
        return False

def criteria_sequentially(data):
    """
    Check that the criteria are in sequential order (no gaps)
    """
    criteria_row = list(data.iloc[1])
        
    criteria_index = [i for i, x in enumerate(criteria_row) if str(x) != 'nan']
    criteria_index = criteria_index[1:]
    for i in range(0,len(criteria_index)-1):
        if criteria_index[i+1] - criteria_index[i] != 1:
            print('Parent criteria are not in sequential order in the input spreadsheet')
            print(f'There is a gap between {criteria_row[criteria_index[i]]} and {criteria_row[criteria_index[i+1]]}.')
            return False
    return True

def sub_criteria_sequentially(data,criteria_number:int,parent_criteria:list):
    """
    Check that the sub-criteria are in sequential order (no gaps)
    """
    for i in range(0,criteria_number):
        sub_criteria_row = list(data.iloc[13+(21*(i))])
        sub_criteria_index = [i for i, x in enumerate(sub_criteria_row) if str(x) != 'nan']
        if len(sub_criteria_index) == 0:
            continue
        elif len(sub_criteria_index) == 1:
            if sub_criteria_index[0] != 7:
                print(f'{sub_criteria_row[sub_criteria_index[0]]} needs to be in the first column in Tier 2.{i+1}')
                return False
        else:
            for j in range(0,len(sub_criteria_index)-1):
                if sub_criteria_index[j+1] - sub_criteria_index[j] != 1:
                    print('Sub-criteria are not in sequential order in the input spreadsheet')
                    print(f'There is a gap between {sub_criteria_row[sub_criteria_index[j]]} and {sub_criteria_row[sub_criteria_index[j+1]]} in Tier 2.{i+1}.')
                    return False
    return True




parents,number = criteria_info(data)
print("Unique parent criteria:", criteria_unique(parents))
print("Criteria match with parent definitions:", parent_match(data,parents,number))
print("Unique sub-criteria:", sub_criteria_unique(data,number))
print("Criteria appear sequentially:", criteria_sequentially(data))
print("Sub-criteria appear sequentially:", sub_criteria_sequentially(data,number,parents))
