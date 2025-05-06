import os
import json
import pandas as pd

# โฟลเดอร์ที่เก็บ JSON
folder_path = r"C:\Users\U s e r\OneDrive\Desktop\DSI324_file\data\3_output\basic_info"

# เก็บผลลัพธ์ที่แตก list แล้ว
rows = []

# วนลูปทุกไฟล์ JSON
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                curr_id = content.get("curr-id", None)
                careers = content.get("careers", [])

                # แยก careers เป็น record ละ 1 แถว
                for career in careers:
                    rows.append({

                        "curr_id": curr_id,
                        "career": career.strip()
                    })
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")

# สร้าง DataFrame จากผลลัพธ์ที่แตก
df = pd.DataFrame(rows)

# แสดงผล
print(df.head())

# (ถ้าต้องการ) export เป็นไฟล์ CSV หรือ Excel
df.to_csv("careers_extracted.csv", index=False)
# df.to_excel("careers_extracted.xlsx", index=False)
