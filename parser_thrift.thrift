namespace java com.myhexin.parser
namespace py parser

############################################################
# dataformats

struct Record{
    1: optional string title,
    2: optional string bodytitle,
    3: optional string content,
    4: optional string pubsource,
    5: optional string pubtime,
    6: optional string author,
}

###########################################################
# service

service ParseService{    
    Record Parse(1:required string url, 2:required string document, 3:required string cg),
    Record Parse2(1:required string url, 2:required string document, 3:required string cg),
    
}
