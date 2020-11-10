


while True:
    try:
        inp = input()

        [N,L,P] = [ int(x) for x in inp.split(' ')]

        qtdAlunosTurma = N // P 
        sobram = 0
        if ( qtdAlunosTurma >= L ):
            qtdAlunosTurma = L
            sobram = N - qtdAlunosTurma * P
        else:
            sobram = N - qtdAlunosTurma * P
            
            cont = P > 1
            while( cont ):
                P = P-1
                qtdAlunosTurma_ = N // P
                sobram_ = N - qtdAlunosTurma_ * P

                cont = P > 1 and qtdAlunosTurma_ < L and qtdAlunosTurma_ != qtdAlunosTurma 

                if ( qtdAlunosTurma_ <= L  and sobram_ < sobram ):
                    qtdAlunosTurma, sobram  = qtdAlunosTurma_, sobram_

        print(qtdAlunosTurma, sobram)
    except:
        break

