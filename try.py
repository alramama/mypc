import pandas as pd
extracted_file=[]
a=['Camera','ISS','Door','Card','Data','blocker-','Video','CCTV','Held','Access','Civil','Crash','Gate','Generic']
for keys in range(len(a)):
    file = pd.read_excel('Jubail Desalination Plant.xlsx')
    df_sheet_index = pd.read_excel('Jubail Desalination Plant.xlsx', sheet_name=1)
    #print(df_sheet_index)
    data = pd.DataFrame(df_sheet_index)
    rows = data.to_numpy()
    for i in rows:
        search = (str(i[0]).split())
        for word in search:
            if a[keys] == word:
                datas= (str(a[keys]).count(a[keys]),a[keys],i)
                extracted_file.append(data)
data = pd.DataFrame(extracted_file)
data.to_excel("output.xlsx")


