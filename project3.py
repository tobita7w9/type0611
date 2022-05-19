def main():
    #ランダムに並べられた重複のない整数の配列
    #array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    array=[5,2,6,26,66,9,3,21,28,61,7,8,85,54]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    #基準値以上:above,above_idx 基準値未満:below,below_idx
    above=None
    below=None
    above_idx=None
    below_idx=None
    array_above=[]
    array_below=[]


    ans=True
    while ans:

        for up in range(len(array)):
            down = len(array)-1-up
            
            #下から上に基準値以上を見つける
            if array[up]>=pivot and above is None:
                above_idx=up
                above=array[above_idx]
            #上から下に基準値未満を見つける
            if array[down]<pivot and below is None:
                below_idx=down
                below=array[below_idx]
            

            if above and below:
                #検索がぶつかったとき
                if above_idx-below_idx==1:
                    array_below=array[:above_idx]
                    array_above=array[above_idx:]

                    if len(array_below)>1:
                        array_below=sort(array_below)
                    if len(array_above)>1:
                        array_above=sort(array_above)

                    ans=False
                    return array_below+array_above

                else:
                    array[above_idx]=below
                    array[below_idx]=above
                    above=None
                    below=None

                break
        else:
            return array    

    # ここまで記述

if __name__ == '__main__':
    main()
