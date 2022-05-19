def main():
    # 昇順にソートされた配列
    #sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    sorted_array=[1,3,4,5,6,8,12,53,65,73,134,567,754,1256,1356,5555,7891,9359]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述    
    array_num=len(sorted_array)
    
    high=array_num
    low=0
    while array_num>=1:
        array_num=len(sorted_array[low:high])
        #中央値のインデックス:mid、値:medium
        mid=array_num//2
        medium=sorted_array[low+mid]

        if medium==target_number:
            return low+mid
        
        elif medium>target_number:
            high=low+mid    
        else:
            low=low+mid+1



    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()