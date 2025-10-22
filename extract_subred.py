import json

all_subreddit_names = []
page = 1

while True:
    try:
        # 嘗試讀取 page1.json, page2.json ...
        filename = f"page{page}.json"
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 提取這一頁的所有 subreddit
        children = data.get('data', {}).get('children', [])
        if not children:
            break # 如果沒有 'children' 了，就停止

        for item in children:
            all_subreddit_names.append(item.get('data', {}).get('display_name'))

        # 檢查是否有下一頁
        if data.get('data', {}).get('after') is None:
            break # 這是最後一頁
        
        page += 1 # 準備讀取下一頁

    except FileNotFoundError:
        # 找不到 pageX.json，說明已經處理完所有文件
        print(f"處理完畢，找不到 {filename}。")
        break
    except Exception as e:
        print(f"讀取 {filename} 時出錯: {e}")
        break

# --- 打印結果 ---
print(f"\n你總共關注了 {len(all_subreddit_names)} 個 Subreddits：\n")
for name in all_subreddit_names:
    print(name)

# --- （可選）保存到一個 .txt 文件 ---
with open("my_subreddits.txt", "w", encoding='utf-8') as f:
    for name in all_subreddit_names:
        f.write(name + "\n")