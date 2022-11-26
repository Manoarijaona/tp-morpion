from case import Case


class CaseStates:
    def __init__(self):
        self.morpionStates = []
        self.resetStates()

    def resetStates(self):
        for i in range(1, 10):
            self.morpionStates.append(Case.isEmpty)

    def updateState(self, case: int, state: Case):
        self.morpionStates[case] = state

    def getCaseStates(self):
        return self.morpionStates
