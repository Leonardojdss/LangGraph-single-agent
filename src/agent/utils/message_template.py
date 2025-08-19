from langchain_core.messages import convert_to_messages

def filter_messages_by_type(messages, message_types=None):
    """
    filter messages per type.
    if None, return all messages.
    """
    if message_types is None:
        return messages
    
    filtered = []
    for msg in messages:
        msg_type = getattr(msg, 'type', 'unknown')
        if msg_type in message_types:
            filtered.append(msg)
    return filtered

def pretty_print_tools_only(update):
    """function especific for show only tool messages"""
    for node_name, node_update in update.items():
        print(f"🔧 Tool messages from node {node_name}:")
        messages = convert_to_messages(node_update["messages"])
        tool_messages = filter_messages_by_type(messages, ['tool'])
        
        if tool_messages:
            for msg in tool_messages:
                pretty_print_message(msg, indent=False)
        else:
            print("No tool messages found.")
        print("\n")

def pretty_print_message(message, indent=False):
    pretty_message = message.pretty_repr(html=True)
    
    if hasattr(message, 'type'):
        message_type = getattr(message, 'type', 'unknown')
        if message_type == 'tool':
            print(f"🔧 TOOL MESSAGE ({getattr(message, 'name', 'unknown_tool')}):")
        elif message_type == 'ai':
            if hasattr(message, 'tool_calls') and message.tool_calls:
                print(f"AI MESSAGE (with {len(message.tool_calls)} tool calls):")
            else:
                print("AI MESSAGE:")
        elif message_type == 'human':
            print("HUMAN MESSAGE:")
        else:
            print(f"{message_type.upper()} MESSAGE:")
    
    if not indent:
        print(pretty_message)
        print("-" * 50)  # visual separator
        return

    indented = "\n".join("\t" + c for c in pretty_message.split("\n"))
    print(indented)
    print("\t" + "-" * 50)  # visual separator indented

def pretty_print_messages(update, last_message=False):
    is_subgraph = False
    if isinstance(update, tuple):
        ns, update = update
        if len(ns) == 0:
            return

        graph_id = ns[-1].split(":")[0]
        print(f"Update from subgraph {graph_id}:")
        print("\n")
        is_subgraph = True

    for node_name, node_update in update.items():
        update_label = f"Update from node {node_name}:"
        if is_subgraph:
            update_label = "\t" + update_label

        print(update_label)
        print("\n")

        messages = convert_to_messages(node_update["messages"])
        
        if last_message:
            messages = messages[-1:]
        
        for m in messages:
            pretty_print_message(m, indent=is_subgraph)
        print("\n")