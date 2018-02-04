from random import randint
import scipy
import csv

def Main():

    with open("./trainingData2.csv", 'w') as csvfile:
        writer = csv.writer(csvfile,str='excel')
        writer.writerow(['leftSensor', 'middleSensor', 'rightSensor', 'left', 'forward', 'right'])
        lines = []



def main():
    with open('./trainingData.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['leftSensor', 'middleSensor', 'rightSensor', 'left', 'forward', 'right'])
        lines = []
        for i in range(150):
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
                row.append(0)
                row.append(0)
                row.append(1)
            elif row[2] < 25:
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
	if sys.argv[1]:
		number = sys.argv[1]
	else:
		number = 150 
    main()
