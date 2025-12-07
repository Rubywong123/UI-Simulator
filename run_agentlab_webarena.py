from agentlab.agents.generic_agent import AGENT_4o_MINI 

from agentlab.experiments.study import make_study

study = make_study(
    benchmark="webarena",  # or "webarena", "workarena_l1" ...
    agent_args=[AGENT_4o_MINI],
    comment="My first study",
)

study.run(n_jobs=4)