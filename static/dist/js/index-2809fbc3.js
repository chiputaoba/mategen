import{d as b,p as d,c as _,b as s,a as o,t as h,F as q,e as A,r as D,o as m,N as v,G as N,C as w,$ as g,w as u,D as F,ar as K,f as L,U as j,_ as z}from"./index-67479de6.js";const G={class:"list-home animated-div"},M={class:"add-text"},O={class:"list"},H=["onClick"],J={class:"item-more-content"},P={class:"el-dropdown-link"},Q={class:"item-opt"},W=["onClick"],X={key:0,class:"item-opt-content-name"},Y={key:1,class:"item-opt-content-name"},Z=["onClick"],ee={class:"item-content item-content-update"},te=b({__name:"index",props:{title:{type:String,default:()=>""},sessionType:{type:String,default:()=>""},list:{type:Array,default:()=>[]}},emits:["addSession","querySession","editSession","editSessionName","deleteSession"],setup(i,{emit:x}){const k=d(),S=d("");d(!1);const a=d(""),B=function(e){S.value=e.id,l("querySession",e)},I=function(){l("addSession")},E=function(e){const t=Object.assign({},e);t.name=a.value,l("editSessionName",t)},U=function(e){e.isUpdate=!1,a.value=""},y=d(),$=function(e,t,r){var p;r==="KB"?(e.isUpdate=!0,a.value=e.name,y.value=t,(p=k.value[t])==null||p.focus()):r==="DB"&&l("editSession",e)},V=function(e){l("deleteSession",e),document.querySelectorAll(".item-more-content-el-dropdown").forEach(function(t){t.style.display="none"})},l=x;return(e,t)=>{const r=K,p=D("Select"),C=L,R=D("CloseBold"),T=j;return m(),_("div",G,[s("div",{class:"add",onClick:I},[o(v,{"icon-class":"layoutAdd",className:"add-svg"}),s("div",M,h(i.title),1)]),s("div",O,[(m(!0),_(q,null,A(i.list,(n,f)=>(m(),_("div",{class:N(["list-item",{"list-item-active":S.value==n.id}]),key:f},[w(s("div",{class:N(["item-content",{"item-content-db":i.sessionType==="DB"}])},[s("div",{class:"item-name",onClick:c=>B(n)},h(n.name),9,H),s("div",J,[o(r,{trigger:"click","popper-class":"item-more-content-el-dropdown",teleported:!1},{dropdown:u(()=>[s("div",Q,[s("div",{class:"item-opt-content",onClick:c=>$(n,f,i.sessionType)},[o(v,{"icon-class":"icon_edit",className:"icon-edit"}),i.sessionType==="KB"?(m(),_("div",X,"重命名")):i.sessionType==="DB"?(m(),_("div",Y,"编辑")):F("",!0)],8,W),s("div",{class:"item-opt-content",onClick:c=>V(n)},[o(v,{"icon-class":"icon_delete",className:"icon-delete"}),t[1]||(t[1]=s("div",{class:"item-opt-content-name"},"删除",-1))],8,Z)])]),default:u(()=>[s("div",P,[o(v,{"icon-class":"itemMore",className:"item-more"})])]),_:2},1024)])],2),[[g,!n.isUpdate||y.value!==f]]),w(s("div",ee,[o(T,{ref_for:!0,ref_key:"updateInputRef",ref:k,modelValue:a.value,"onUpdate:modelValue":t[0]||(t[0]=c=>a.value=c),style:{width:"100%"},placeholder:"请输入",class:"edit-input-item"},{suffix:u(()=>[o(C,{color:"#D0D5DE",class:"edit-item-suffix-icon",onClick:c=>E(n),style:{cursor:"default"}},{default:u(()=>[o(p)]),_:2},1032,["onClick"]),o(C,{color:"#D0D5DE",style:{"margin-left":"6px",cursor:"default"},class:"edit-item-suffix-icon",onClick:c=>U(n)},{default:u(()=>[o(R)]),_:2},1032,["onClick"])]),_:2},1032,["modelValue"])],512),[[g,n.isUpdate&&y.value===f]])],2))),128))])])}}});const oe=z(te,[["__scopeId","data-v-35aa9fc5"]]);export{oe as S};
