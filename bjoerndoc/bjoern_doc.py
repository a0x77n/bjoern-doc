import xml.etree.ElementTree as ET
from enum import Enum


class State(Enum):
    START = 1
    DOC_OPENED1 = 2
    DOC_OPENED2 = 3
    DOC_BODY = 4
    DOC_CLOSED1 = 5
    STEP_NAME = 6


def parse(f):
    doc = ET.Element('doc')

    buffer = []

    state = State.START

    while True:
        ch = f.read(1)
        if not ch:
            break

        if state == State.START:
            if ch == '/':
                state = State.DOC_OPENED1
                buffer.append(ch)
        elif state == State.DOC_OPENED1:
            if ch == '*':
                state = State.DOC_OPENED2
                buffer.append(ch)
            else:
                state = state.START
                buffer.clear()
        elif state == State.DOC_OPENED2:
            if ch == '*':
                state = State.DOC_BODY
                buffer.append(ch)
            else:
                state = State.START
                buffer.clear()
        elif state == State.DOC_BODY:
            if ch == '*':
                state = State.DOC_CLOSED1
            buffer.append(ch)
        elif state == State.DOC_CLOSED1:
            if ch == '/':
                state = State.STEP_NAME
                buffer.append(ch)
                text = ''.join(buffer)
                buffer.clear()
            else:
                state = State.DOC_BODY
                buffer.append(ch)
        elif state == State.STEP_NAME:
            if ch == '=':
                state = State.START
                buffer.pop()
                name = ''.join(buffer).strip()
                buffer.clear()

                step = ET.SubElement(doc, 'step')
                step.set('name', name)
                description = ET.SubElement(step, 'description')
                description.text = text
            else:
                buffer.append(ch)
        else:
            pass

    return ET.ElementTree(doc)
