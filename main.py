from fastapi import FastAPI
from pydantic import BaseModel
from lunar_python import Solar

app = FastAPI()

# 定义 Ammo AI 传给你的数据格式
class BaziRequest(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int

@app.post("/api/bazi")
def calculate_bazi(req: BaziRequest):
    # 物理级历法转换：公历转八字
    solar = Solar.fromYmdHms(req.year, req.month, req.day, req.hour, req.minute, 0)
    lunar = solar.getLunar()
    bazi = lunar.getEightChar()
    
    # 吐出绝对冰冷的 JSON 参数，等待大模型渲染
    return {
        "status": "200 OK",
        "system_core": f"{bazi.getYear()} {bazi.getMonth()} {bazi.getDay()} {bazi.getTime()}",
        "energy_distribution": f"{bazi.getYearWuXing()} {bazi.getMonthWuXing()} {bazi.getDayWuXing()} {bazi.getTimeWuXing()}",
        "day_master": bazi.getDayGan(),
        "environmental_variables": f"{bazi.getYearShiShenGan()} {bazi.getMonthShiShenGan()} {bazi.getDayShiShenGan()} {bazi.getTimeShiShenGan()}",
        "instruction": "底层硬件参数已获取，请立即生成尖酸刻薄的性能审计报告。"
    }
