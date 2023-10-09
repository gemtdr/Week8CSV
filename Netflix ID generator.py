
def read_in_file(filename):

    info = []

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        print(reader)
        for row in reader:
            info.append((row[2], row[4]))

    return info



if __name__ == "__main__":


    import csv

    filename = "netflix_titles.csv"

    name = input('Enter the name of an actor or actress ==> ')

    print()

    info = read_in_file(filename)

    print(f'{name} has been in: ')

    print()
          

    for tuplepair in info:

        if name in tuplepair[1]:

            print(tuplepair[0])

   

    
