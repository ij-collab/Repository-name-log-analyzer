# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:49:18 2026

@author: user
"""



from pathlib import Path

log_file = Path("system.log")

if not log_file.exists():
    print("system.log が見つかりません")
else:
    text = log_file.read_text(encoding="utf-8")
    
    error_count = text.count("ERROR")
    info_count = text.count("INFO")
    warning_count = text.count("WARNING")
    
    print("=" * 30)
    print("LOG ANALYZER")
    print("=" * 30)
    
    print("ログ解析結果")
    print(f"ERROR: {error_count}件")
    print(f"INFO: {info_count}件")
    print(f"WARNING: {warning_count}件")
    
    if error_count > 0:
        print("異常があります")
    else:
        print("異常はありません")
        
    print("\nERRORの内容")
    
    for line in text.splitlines():
        if "ERROR" in line:
            print(line)
    
    print("\nWARNINGの内容")
    
    for line in text.splitlines():
        if "WARNING" in line:
            print(line)
            
    result = open("analysis_result.txt", "w", encoding="utf-8")
    result.write(f"ERROR: {error_count}件\n")
    result.write(f"INFO:{info_count}件\n")
    result.write(f"WARNING: {warning_count}件\n")
    result.close()
    
                