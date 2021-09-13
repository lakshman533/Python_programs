N,M=map(int,input().split())
pattern=[('.|.'*(2*i-1)).center(M,"-") for i in range(1,(N//2)+1)]
print('\n'.join(pattern+["WELCOME".center(M,"-")]+pattern[::-1]))
