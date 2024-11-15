import sys

def functionLoader():
    global Variable, Utilities
    sys.path.append(sys.path[0] + "/..")
    import Variable, Utilities

def dataConcatenation(task, data):
    folder_path = Variable.CONCATFOLDERPATH
    data_list = []
    for file_name in data:
        data_list += Utilities.dataLoader(folder_path, file_name)

    concatenated_data = Utilities.dataConcatenation(data_list)
    Utilities.storeDataInYears(concatenated_data, f"{task}", 'Concat 2015-2022')

def main(task, data):
    functionLoader()
    dataConcatenation(task, data)