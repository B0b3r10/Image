"""syntax = "proto3";
message Image {
    int32 id = 1;
    bytes data = 2;
    int32 width = 3;
    int32 height = 4;
    //int32 channels = 5;
  }"""
import sendImg_pb2
image = sendImg_pb2.Image()
image.id = 1234
image.data(65419)
image.width(600)
image.height(400)
