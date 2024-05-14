from __future__ import annotations

import logging
import multiprocessing
import time
from multiprocessing import Queue
from typing import Iterable


class BaseNode:
    def __init__(self, inputs: Iterable[str], outputs: Iterable[str]):
        self.inputs = tuple(inputs)
        self.outputs = tuple(outputs)

        self.input_connections: dict[str, tuple[Queue, BaseNode, str]] = {i: (Queue(), None, "") for i in self.inputs}
        self.output_connections: dict[str, set[tuple[Queue, BaseNode, str]]] = {i: set() for i in outputs}

        self.input_values = {}
        self.output_results = {}

    def start(self):
        process = multiprocessing.Process(target=self._serve)
        process.start()

    def _producers_are_ready(self):
        for input in self.inputs:
            if self.input_connections[input][0].empty():
                return False
        return True

    def _consumers_are_ready(self):
        for output in self.outputs:
            for acceptor in self.output_connections[output]:
                if not acceptor[0].empty():
                    return False
        return True

    def _send_to_consumers(self):
        for output in self.outputs:
            for consumer in self.output_connections[output]:
                consumer[0].put(self.output_results[output])

        self.output_results.clear()

    def _get_from_producers(self):
        for input in self.inputs:
            self.input_values[input] = self.input_connections[input][0].get()

    def _results_are_ready(self):
        return len(self.output_results.keys()) != 0

    def _serve(self):
        while True:
            time.sleep(0.5)
            if self._results_are_ready():
                if self._consumers_are_ready():
                    self._send_to_consumers()
                else:
                    continue

            if self._producers_are_ready():
                self._get_from_producers()
                self.process()

    def process(self):
        pass

    def _get_input(self, input: str):
        return self.input_connections[input][0].get()

    def send_output(self, output: str, value):
        self.output_results[output] = value

    def bind_o2i(self, output, node: BaseNode, input):
        if output not in self.outputs:
            logging.error(f'Output "{output}" is not in {self} outputs')
        if input not in node.inputs:
            logging.error(f'Input "{input}" is not in {node} inputs')

        q = Queue()
        self.output_connections[output].add((q, node, input))
        node.input_connections[input] = (q, self, output)

    def __hash__(self):
        return hash((self.inputs, self.outputs))
