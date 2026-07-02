def parse_sse(raw: str) -> list[dict]:
    events = []
    current_event = None
    current_data = None

    for line in raw.split("\n"):
        line = line.strip()
        if line.startswith("event:"):
            current_event = line[len("event:"):].strip()
        elif line.startswith("data:"):
            current_data = line[len("data:"):].strip()
        elif line == "":
            # 空行表示一个事件结束
            if current_event is not None and current_data is not None:
                if current_data != "[DONE]":
                    events.append({"event": current_event, "data": current_data})
            current_event = None
            current_data = None

    # 处理末尾没有空行的情况
    if current_event is not None and current_data is not None:
        if current_data != "[DONE]":
            events.append({"event": current_event, "data": current_data})

    return events
