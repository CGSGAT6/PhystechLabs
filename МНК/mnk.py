import numpy as np

def write_mnk( in_file_name = "in.txt", out_file_name = "out.txt" ):
    with open(in_file_name, "r") as f:
        is_intersects_zero = f.readline().strip("\n").lower()
        N = int(f.readline())
        abscisses = np.zeros(N)
        ordinates = np.zeros(N)
        for i in range(N):
            s = f.readline()
            abscisses[i] = float(s.replace(",", "."))
        for i in range(N):
            s = f.readline()
            ordinates[i] = float(s.replace(",", "."))

    #print(abscisses)
    #print(ordinates)

    if is_intersects_zero == "false" or is_intersects_zero == "0":
        x_aver = np.mean(abscisses)
        y_aver = np.mean(ordinates)

        xsxa = abscisses - x_aver
        ysya = ordinates - y_aver

        D = np.sum(xsxa * xsxa)

        B = np.sum(xsxa * ysya) / D
        A = y_aver - x_aver * B

        d_arr = ordinates - (abscisses * B + A)
        sumd2 = np.sum(d_arr * d_arr)
        Sb2 = 1 / D * sumd2 / (N - 2)
        Sa2 = ((x_aver ** 2) / D + 1 / N) * sumd2 / (N - 2)
        with open(out_file_name, "w") as f:
            f.write("Equtation form: y = A + B * x\n")
            f.write(f"A = {A}\nB = {B}\nSa^2 = {Sa2}\nSb^2 = {Sb2}")
    else:
        sumx2 = np.sum(abscisses * abscisses)
        B = np.sum(abscisses * ordinates) / sumx2
        d_arr = ordinates - (abscisses * B)
        Sb2 = np.sum(d_arr * d_arr) / sumx2 / (N - 1)
        with open(out_file_name, "w") as f:
            f.write("Equtation form: y = B * x\n")
            f.write(f"B = {B}\nSb^2 = {Sb2}")
                


write_mnk(*input("Enter file names: ").split())
