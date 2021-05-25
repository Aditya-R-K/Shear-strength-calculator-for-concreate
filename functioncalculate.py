import pandas as pd
import os

#whole chart wriiten in 2d-list as name "table"
table = {
    "Index": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Value": [0.15, 0.25, 0.5, 0.75, 1.00, 1.25, 1.5, 1.75, 2.00, 2.25, 2.5, 2.75, 3.00],
    "M15": [0.28, 0.35, 0.46, 0.54, 0.6, 0.64, 0.68, 0.71, 0.71, 0.71, 0.71, 0.71, 0.71],
    "M20": [0.28, 0.36, 0.48, 0.56, 0.62, 0.67, 0.72, 0.75, 0.79, 0.81, 0.82, 0.82, 0.82],
    "M25": [0.29, 0.36, 0.49, 0.57, 0.64, 0.7, 0.74, 0.78, 0.82, 0.85, 0.88, 0.9, 0.92],
    "M30": [0.29, 0.37, 0.5, 0.59, 0.66, 0.71, 0.76, 0.8, 0.84, 0.88, 0.91, 0.94, 0.96],
    "M35": [0.29, 0.37, 0.5, 0.59, 0.67, 0.73, 0.78, 0.82, 0.86, 0.9, 0.93, 0.96, 0.99],
    "M40": [0.3, 0.38, 0.51, 0.6, 0.68, 0.74, 0.79, 0.84, 0.88, 0.92, 0.95, 0.98, 1.01]
}
#Dataframe of table
df = pd.DataFrame(table)

#Main Function
def toc_calculate(Iv: float, Ig: str):
    if (Iv > 3.00) or (Iv == 0) or (Iv < 0) or (Ig == "") or ((Ig != "M15") and (Ig != "M20") and (Ig != "M25") and (Ig != "M30") and (Ig != "M35") and (Ig != "M40")) or (Iv == ""):
        return 0
    else:
        try:
            if Iv < 0.15:
                ValueIndex = df[df.Value == 0.15]["Index"].values[0]
                finalans = df.at[ValueIndex, Ig]
                os.system("cls")
                print("=========================================================================")
                print("\t\tValue is less than 0.15")
                print("=========================================================================")
                print("%PT value considered  = 0.15", "\tInput value  =", Iv)
                print("Grade value  =", Ig)
                print("Final answer =", finalans)
                print("=========================================================================")
                return finalans
            if Iv >= 0.15:
                ValueIndex = df[df.Value == Iv]["Index"].values[0]
                finalans = df.at[ValueIndex, Ig]
                os.system("cls")
                print("=========================================================================")
                print("\tExact Match Found in table")
                print("=========================================================================")
                print("Input value  =", Iv)
                print("Grade value  =", Ig)
                print("Final answer =", finalans)
                print("=========================================================================")
                return finalans
        except IndexError:
            hdf = df[df['Value'] > Iv]
            hdf = hdf.reset_index(drop=True)
            ldf = df[df['Value'] < Iv]
            ldf = ldf.loc[::-1]
            ldf = ldf.reset_index(drop=True)
            # global LPT,HPT,HIg,LIg,xvalue
            LPT = ldf.at[0, 'Value']
            HPT = hdf.at[0, 'Value']
            LIg = ldf.at[0, Ig]
            HIg = hdf.at[0, Ig]
            xvalue = (((HIg - LIg) * (Iv - LPT)) / (HPT - LPT))
            finalans = xvalue + LIg
            os.system("cls")
            print("=========================================================================")
            print("\tExact Match Found in table")
            print("=========================================================================")
            print("Lower PT Value  =", LPT, "\tLower grade value  =", LIg)
            print("Higher PT Value =", HPT, "\tHigher grade Value =", HIg)

            print("\n\t\t   (HIg - LIg) X (PTvalue - LPT)")
            print("Value of x =   __________________________________   + LIg")
            print("\t\t\t (HPT - LPT)")

            print(f"\n\t\t  ({HIg} - {LIg}) X ({Iv} - {LPT})")
            print(f"Value of x =   __________________________________   + {LIg}")
            print(f"\t\t\t ({HPT} - {LPT})")

            print(f"\n\t\t  ({HIg - LIg}) X ({Iv - LPT})")
            print(f"Value of x =   __________________________________   + {LIg}")
            print(f"\t\t\t ({HPT - LPT})")

            print(f"\n\t\t  {(HIg - LIg) * (Iv - LPT)}")
            print(f"Value of x =   _______________________________   + {LIg}")
            print(f"\t\t\t {(HPT - LPT)}")

            print(f"\nValue of x = {(((HIg - LIg) * (Iv - LPT)) / (HPT - LPT))} + {LIg}")

            print(f"\nValue of x = {finalans}")

            print("=========================================================================")
            print("Input value  =", Iv)
            print("Grade value  =", Ig)
            print("Final answer =", finalans)
            print("=========================================================================")
            return finalans
        except Exception:
            return 0