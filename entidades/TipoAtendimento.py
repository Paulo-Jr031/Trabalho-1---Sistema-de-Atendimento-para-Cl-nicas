class TipoAtendimento:
    def __init__(self, tipo_atendimento: str):
        self.__tipo_atendimento = tipo_atendimento

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento):
        if not tipo_atendimento.strip():
            raise ValueError('O tipo de atendimento não pode ser vazio!')
        self.__tipo_atendimento = tipo_atendimento