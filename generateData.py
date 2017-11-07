from random import randint
import scipy
import csv



def main():
    with open('./trainingData.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        lines = []
        for i in range(300):
            row = []
            for j in range(3):
                row.append(randint(15, 100))

            if row[1] < 25:
                if row[0] >= row[2]:
                    row.append(1)
                    row.append(0)
                    row.append(0)
                elif row[0] < row[2]:
                    row.append(0)
                    row.append(0)
                    row.append(1)
            elif row[0] < 25:
                if row[1] >= row[2]:
                    row.append(0)
                    row.append(1)
                    row.append(0)
                elif row[1] < row[2]:
                    row.append(0)
                    row.append(0)
                    row.append(1)
            elif row[2] < 25:
                if row[1] >= row[0]:
                    row.append(0)
                    row.append(1)
                    row.append(0)
                elif row[1] < row[0]:
                    row.append(1)
                    row.append(0)
                    row.append(0)
            else:
                row.append(0)
                row.append(1)
                row.append(0)

            lines.append(row)

        for line in lines:
            writer.writerow(line)


    return 0

if __name__ == '__main__':
    main()