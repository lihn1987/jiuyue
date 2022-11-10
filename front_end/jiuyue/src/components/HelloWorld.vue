<template>
  <div height="100%">
    <el-container style="width:100%">
      <el-aside width="200px"  :style="'background:#ff0000;width:180px;background:#333333;height:'+screen_height+'px'">
        <div style="background:#222222;padding-top:16px; padding-bottom: 15px;">
          <div style="width:56px; height:56px; background-image: url('/static/logo.png');background-size: cover;margin-left:62px"></div>
          <div style="font-size:12px;line-height: 17px; color:#888888;margin-top:8px; letter-spacing:4px;">九月PPT网址导航</div>
        </div>
        <div v-for="n in type_list.length" :class="n == current_index ? 'type1_active': 'type1_default'"  @click="click_type(n)"> 
          {{type_list[n-1].name}}
        </div>
      </el-aside>
      <el-main :style="'background:#F4F4F4;padding:24px 40px 24px 32px;height:'+screen_height+'px;overflow-y: auto'">

        <div v-for="i in type_list.length" style="background: #FFFFFF;border-radius: 8px;margin-top:24px;padding-bottom: 20px;"> 
          <div style="text-align:left; padding-top:16px;padding-left:24px;font-size:16px">{{type_list[i-1]["name"]}}</div>
 
          <el-row v-for="j in (Math.floor((type_list[i-1]['list'].length-1)/6)+1)" :gutter="12" class="row" :key="j">
            <el-col v-for="k in (type_list[i-1]['list'].length - (j-1)*6) > 6?6:(type_list[i-1]['list'].length - (j-1)*6)" :span="4" ><div >
              <div class="item_box" @click="click_item(i, j)">
                <el-container style="padding:8px" >
                  <el-aside width="26px" >
                    <div class = "item_logo" style="background-image: url('/static/logo.png')"></div>
                  </el-aside>
                  <el-main style="padding:0 0 0 8px">
                    <div class ="item_title">{{type_list[i-1]['list'][(j-1)*6+k-1].name}}</div>
                    <div class="item_des">{{type_list[i-1]['list'][(j-1)*6+k-1].desc}}</div>
                  </el-main>
                </el-container>
              </div>
            </div></el-col>
          </el-row>

        </div>  

      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      screen_height: 0,
      current_index: 1,
      type_list: []
    }
  },
  mounted: function(){
    var self = this
    self.screen_height = window.innerHeight
    window.onresize = () => {
      return (() => {
        self.screen_height = window.innerHeight
      })()
    }
    console.log((Math.floor((0-1)/6)+1))
    this.FlushType1()
  },
  methods: {
    FlushType1: function() {
      var self = this
      axios.get("/jiuyue/get_type1_list").then(function(data){
        self.type_list = data.data.data
        console.log(self.type_list)
        console.log(self.type_list.length)
      })
    },
    click_type: function(n){
      this.current_index = n
      console.log(n)
    },
    click_item: function(i, j) {
      window.open(this.type_list[i-1]['list'][j-1].url)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.type1_active {
  background:#222222;
  color:#A8D48E;
  margin-top:8px;
  line-height: 40px;
  font-size: 14px;
}

.type1_default:hover {
  background:#222222;
  color:#A8D48E;
  margin-top:8px;
  line-height: 40px;
  font-size: 14px;
  border-left: 6px solid #87c264;
  border-right: 6px solid #87c26400;
}
.type1_default {
  color:#DDDDDD;
  margin-top:8px;
  line-height: 40px;
  font-size: 14px;
}


.row {
  margin-left:24px; 
  margin-right:24px; 
  margin-top:12px;
  padding-left:16px;
  padding-right: 24px;
}
.item_logo{
  width:26px;
  height:26px;
  background-size: cover;
}
.item_box:hover{
  border-radius: 3px;
  background:#f4f4f4;
}
.item_title{
  text-align: left;
  font-size: 14px;
  line-height:19px;
  color:#333333;
  overflow: hidden;
  text-overflow: ellipsis;
}

.item_des{
  margin-top: 4px;
  text-align: left;
  word-break:break-all;
  height: 32px;
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; 
  font-size:12px; 
  color:#777777
}
</style>
