N=int(input("N = ")) # taking the input from the user => N=5
M=3*N  #  M is 3 times N 
print("M =",M) #print M value => M=15  
string="WELCOME" # enter a string value  =>WELCOME
n=len(string) # len() -returns the length of the string  => n=7
d=0 # for string indexing, intialize d value to 0 
c=(M-n)//2 # c=(15-7)//2 = (8)//2 = 4 => c=4 
f=N//2 # f is the row index at which the "welcome" message must be printed  => f=2
if N%2!=0: # N must be odd (according to the question)
    for i in range(N):
        for j in range(M):
            if j==0 or j==M-1 or i==0 or i==N-1 or j<c:
                print(".",end=" ") # print("|",end=" ") or print("-",end=" ")
            else:
                if f==i and d<n:
                    print(string[d],end=" ")
                    d+=1
                else:
                    # after the welcome message is printed , 4 dots must be printed
                    print(".",end=" ")
        print("")
