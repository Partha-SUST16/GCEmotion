class CommitMessage:
    def __init__(self, encoded_message):
        self.encoded_message = encoded_message
        self.commit_title = ''
        self.commit_body = ''

    def get_commit_title(self):
        commit_title = self.to_string().splitlines()[0]
        return commit_title

    def get_commit_body(self):
        body_lines = self.to_string().splitlines()
        if len(body_lines) <= 1:
            return self.commit_body
        else:
            body_lines.pop(0)
            return '\n'.join(body_lines)

    def to_string(self):
        decoded_message = bytes.fromhex(self.encoded_message).decode('utf-8')
        return decoded_message


# one_line_commit = '4920616d206120636f6d6d6974206d6573736167652e'[2:]
# three_line_commit = "4920616d206120636f6d6d6974206d6573736167652e0d0a546869732069732074686520326e64206c696e652e0d0a5468697320697320337264206c696e652e"[
#                     2:]
#
# # p1 = CommitMessage(three_line_commit)
# p1 = CommitMessage(one_line_commit)
#
# # print(p1.to_string())
# print('Title=' + p1.get_commit_title())
# print('Body=' + p1.get_commit_body())
