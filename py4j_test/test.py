# -*- coding:utf-8 -*-
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

stack = gateway.entry_point.getStack()
stack.push("First %s" % ('item'))
stack.push("Second item")
stack.pop()

stack.push('First item')

internal_list = stack.getInternalList()

print(len(internal_list))
print(internal_list[0])

internal_list.append('Second item')

print(internal_list)

print(stack.getInternalList())

sliced_list = internal_list[0:1]

print(sliced_list)

sliced_list.append('Third item')

print(sliced_list)

print(internal_list)

print(stack.getInternalList())

stack.pushAll(sliced_list)

print(stack.getInternalList())