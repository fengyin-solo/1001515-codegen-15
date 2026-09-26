"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class FlightEntry(BaseModel):
    """航班明细结构。"""

    field_0: str | None = None  # 航班号
    field_1: str | None = None  # 航空公司
    field_2: str | None = None  # 机型
    field_3: str | None = None  # 进港时刻
    field_4: str | None = None  # 出港时刻
    field_5: str | None = None  # 机位号码
    field_6: str | None = None  # 上下客人数
    field_7: str | None = None  # 航班状态

class StandEntry(BaseModel):
    """停机位明细结构。"""

    field_0: str | None = None  # 机位编号
    field_1: str | None = None  # 机位类型
    field_2: str | None = None  # 适用机型
    field_3: str | None = None  # 当前航班
    field_4: str | None = None  # 占用时段
    field_5: str | None = None  # 释放时刻
    field_6: str | None = None  # 廊桥状态
    field_7: str | None = None  # 机位状态

class BaggageEntry(BaseModel):
    """行李转运单明细结构。"""

    field_0: str | None = None  # 转运单号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 行李类型
    field_3: str | None = None  # 始发站
    field_4: str | None = None  # 目的地
    field_5: str | None = None  # 件数预估
    field_6: str | None = None  # 实际件数
    field_7: str | None = None  # 转运状态

class BridgeEntry(BaseModel):
    """廊桥明细结构。"""

    field_0: str | None = None  # 廊桥编号
    field_1: str | None = None  # 对接机位
    field_2: str | None = None  # 对接型号
    field_3: str | None = None  # 靠桥时刻
    field_4: str | None = None  # 撤离时刻
    field_5: str | None = None  # 操作员
    field_6: str | None = None  # 维护周期
    field_7: str | None = None  # 廊桥状态

class StairsEntry(BaseModel):
    """客梯车明细结构。"""

    field_0: str | None = None  # 车牌号
    field_1: str | None = None  # 车辆型号
    field_2: str | None = None  # 梯高上限
    field_3: str | None = None  # 驾驶员
    field_4: str | None = None  # 指派机位
    field_5: str | None = None  # 抵达时刻
    field_6: str | None = None  # 撤离时刻
    field_7: str | None = None  # 车辆状态

class RefuelAviationEntry(BaseModel):
    """加油作业单明细结构。"""

    field_0: str | None = None  # 加油单号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 油料类型
    field_3: str | None = None  # 加油量
    field_4: str | None = None  # 加油车编号
    field_5: str | None = None  # 加油员
    field_6: str | None = None  # 开始时刻
    field_7: str | None = None  # 结束时刻

class WaterEntry(BaseModel):
    """加注作业单明细结构。"""

    field_0: str | None = None  # 加注单号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 加注量
    field_3: str | None = None  # 加水车编号
    field_4: str | None = None  # 操作员
    field_5: str | None = None  # 开始时刻
    field_6: str | None = None  # 结束时刻
    field_7: str | None = None  # 加注状态

class LavatoryEntry(BaseModel):
    """排污作业单明细结构。"""

    field_0: str | None = None  # 排污单号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 排污车编号
    field_3: str | None = None  # 操作员
    field_4: str | None = None  # 开始时刻
    field_5: str | None = None  # 结束时刻
    field_6: str | None = None  # 消毒记录
    field_7: str | None = None  # 排污状态

class CateringEntry(BaseModel):
    """配餐单明细结构。"""

    field_0: str | None = None  # 配餐单号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 餐食类型
    field_3: str | None = None  # 份数
    field_4: str | None = None  # 配餐车编号
    field_5: str | None = None  # 配送员
    field_6: str | None = None  # 送达时刻
    field_7: str | None = None  # 配餐状态

class DeicingEntry(BaseModel):
    """除冰作业单明细结构。"""

    field_0: str | None = None  # 除冰单号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 除冰液类型
    field_3: str | None = None  # 用量
    field_4: str | None = None  # 除冰车编号
    field_5: str | None = None  # 操作员
    field_6: str | None = None  # 开始时刻
    field_7: str | None = None  # 结束时刻

class PushbackEntry(BaseModel):
    """推车作业单明细结构。"""

    field_0: str | None = None  # 推车单号
    field_1: str | None = None  # 航班号
    field_2: str | None = None  # 拖车编号
    field_3: str | None = None  # 牵引杆编号
    field_4: str | None = None  # 操作员
    field_5: str | None = None  # 推车方向
    field_6: str | None = None  # 开始时刻
    field_7: str | None = None  # 结束时刻

class GpuEntry(BaseModel):
    """电源车明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 电源类型
    field_2: str | None = None  # 额定功率
    field_3: str | None = None  # 驾驶员
    field_4: str | None = None  # 指派机位
    field_5: str | None = None  # 接电时刻
    field_6: str | None = None  # 断电时刻
    field_7: str | None = None  # 车辆状态

class AcuEntry(BaseModel):
    """空调车明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 制冷功率
    field_2: str | None = None  # 制热功率
    field_3: str | None = None  # 驾驶员
    field_4: str | None = None  # 指派机位
    field_5: str | None = None  # 接驳时刻
    field_6: str | None = None  # 撤离时刻
    field_7: str | None = None  # 车辆状态

class RampEntry(BaseModel):
    """巡检记录明细结构。"""

    field_0: str | None = None  # 巡检编号
    field_1: str | None = None  # 巡检区域
    field_2: str | None = None  # 巡检时段
    field_3: str | None = None  # 巡检人员
    field_4: str | None = None  # 道面状况
    field_5: str | None = None  # 标识标线
    field_6: str | None = None  # 外来物
    field_7: str | None = None  # 巡检状态

class FodbEntry(BaseModel):
    """外来物记录明细结构。"""

    field_0: str | None = None  # 排查编号
    field_1: str | None = None  # 发现位置
    field_2: str | None = None  # 物品类型
    field_3: str | None = None  # 风险等级
    field_4: str | None = None  # 发现人员
    field_5: str | None = None  # 发现时刻
    field_6: str | None = None  # 清除时刻
    field_7: str | None = None  # 排查状态

class BoardGateEntry(BaseModel):
    """登机口明细结构。"""

    field_0: str | None = None  # 登机口编号
    field_1: str | None = None  # 所在航站楼
    field_2: str | None = None  # 适用航班
    field_3: str | None = None  # 分配时段
    field_4: str | None = None  # 旅客容量
    field_5: str | None = None  # 登机桥状态
    field_6: str | None = None  # 释放时刻
    field_7: str | None = None  # 口位状态

class CrewGroundEntry(BaseModel):
    """地勤人员明细结构。"""

    field_0: str | None = None  # 员工编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 工种岗位
    field_3: str | None = None  # 所属班组
    field_4: str | None = None  # 上岗资质
    field_5: str | None = None  # 资质到期日
    field_6: str | None = None  # 当班状态
    field_7: str | None = None  # 联系电话

class EquipmentGroundEntry(BaseModel):
    """地勤设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 所属部门
    field_5: str | None = None  # 上次保养日
    field_6: str | None = None  # 下次保养日
    field_7: str | None = None  # 设备状态
