prix=[7,1,5,3,6,4]
def maxProfit(prix):
        gr=0
        n=len(prix)
        for i in range(n):
            for j in range(0,(n-i-1)):
                gr1=prix[j+1]-prix[j]
                prix[j], prix[j+1] = prix[j+1], prix[j]
                if (gr1 >=gr):
                    gr=gr1

        if (gr>=0):
            print(gr)
        else:
            print("0")
        return 0


maxProfit(prix)