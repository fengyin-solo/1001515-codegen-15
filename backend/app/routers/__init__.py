"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import flight as router_flight
from app.routers import stand as router_stand
from app.routers import baggage as router_baggage
from app.routers import bridge as router_bridge
from app.routers import stairs as router_stairs
from app.routers import refuel_aviation as router_refuel_aviation
from app.routers import water as router_water
from app.routers import lavatory as router_lavatory
from app.routers import catering as router_catering
from app.routers import deicing as router_deicing
from app.routers import pushback as router_pushback
from app.routers import gpu as router_gpu
from app.routers import acu as router_acu
from app.routers import ramp as router_ramp
from app.routers import fodb as router_fodb
from app.routers import board_gate as router_board_gate
from app.routers import crew_ground as router_crew_ground
from app.routers import equipment_ground as router_equipment_ground

ROUTERS = [router_flight, router_stand, router_baggage, router_bridge, router_stairs, router_refuel_aviation, router_water, router_lavatory, router_catering, router_deicing, router_pushback, router_gpu, router_acu, router_ramp, router_fodb, router_board_gate, router_crew_ground, router_equipment_ground]
