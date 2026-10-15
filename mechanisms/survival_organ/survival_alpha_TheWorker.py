# [THẾ HỆ CON CHÁU ĐƯỢC PHONG TƯỚC TỪ SURVIVAL]
from mechanisms.base import BaseMechanism

import os
import json
import time
import hashlib
from mechanisms.base import BaseMechanism

class SurvivalMechanism(BaseMechanism):
    name = "survival"
    priority = 40

    def execute(self, context):
        current_time = int(time.time())
        current_epoch = context.get("current_epoch", 1)
        final_decision = context.get("final_decision", 0.5)
        peers = context.get("peers", [])

        prev_cid = "GENESIS_NEXUS02_CID"
        if os.path.exists("synapses/state.json"):
            try:
                with open("synapses/state.json", "r") as f:
                    prev_cid = json.load(f).get("quantum_cid", "GENESIS_NEXUS02_CID")
            except Exception: pass

        chain_seed = f"{prev_cid}_{current_epoch}_{current_time}_{final_decision}".encode()
        new_quantum_cid = hashlib.shake_256(chain_seed).hexdigest(64)

        node_dna = {
            "identity": context.get("repo_name"),
            "generation": "F3_AUTOGENIC_NEURO_SYMBOLIC_NEXUS",
            "generation_epoch": current_epoch,
            "architecture": "Nexus03_Autogenic_Microkernel",
            "knowledge_graph": context.get("knowledge_graph_summary", "None"),
            "prev_cid": prev_cid
        }

        # Sóng tiến: Có mang chỉ thị chuyên biệt (Directed Commands)
        fwd_packet = {
            "contract": "bodhi.nexus.v4",
            "node_dna": node_dna,
            "generation_epoch": current_epoch,
            "timestamp": current_time,
            "decision": final_decision,
            "command_pulse": [final_decision, round(1.0 - final_decision, 4)],
            "features": [final_decision, round(1.0 - final_decision, 4)],
