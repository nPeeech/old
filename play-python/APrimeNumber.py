for i in range(1000):
    n = i+2 #数値をゼロで割るのを避けるため2からスタート i=1だよ
    a = n-1 #変数mは結局使ってないよー!
    m = 'no'
    if n == 2:
        print(n)
    if n%2 == 0:#２で割れる場合は時間短縮のため弾く（２で割れるということは偶数）
        m='No'
    else:
        while n%a > 0:
            a=a-1
            if a==1:
                m = 'Yes'
                print(n)
                break#ループから抜け出す
