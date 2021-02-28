class Contato:
    todos_contatos = []

    def __init__(self, email, linkedin, github):
        self.email = email
        self.linkedin = linkedin
        self.github = github
        self.todos_contatos.append(self)

    def getEmail(self):
        return self.email

    def getLinkedin(self):
        return self.linkedin

    def getGithub(self):
        return self.github

    def setEmail(self, email):
        self.email = email

    def setLinkedin(self, linkedin):
        self.linkedin = linkedin

    def setGithub(self, github):
        self.github = github
