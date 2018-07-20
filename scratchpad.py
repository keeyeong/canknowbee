import facebook

token = 'EAAadwm7tIy8BADIwBc6CUisIxVuLhEiIFQO2iHLAmyigsZAeODmtU9gGlFT9Jbd8OEmYMjCNWzFLO74mmiblvEL1I8rH13oVr97kd4WwwQiYXZAlL5if2xUVOLZC9FWnZAdnOVwWDluCPHUmGfWd8IhSjonRTmcWSDtxWUibZA7pzXTXZBXAZAf4X45KfKl7GlzCD9FXT8wnHlZAmN0poMVJmJv7GS3OYEZA6ty7sx1a0UZBQ2YzFo7gp7'
# token = '1862308270514991|x3qQfT3l8QjYM_e_2bxM0HpwKHc'

graph = facebook.GraphAPI(access_token=token, version=2.7)
#result = graph.request('/search?q=Metal&type=event&limit=10')
result = graph.request('/Buzzcapture')
graph.get_object()
print(result)
