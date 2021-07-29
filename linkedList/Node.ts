class Node {
    private value
    private next
    constructor(value:any,next:Node | null=null){
        this.value = value;
        this.next = next ;
    }
    get nodeValue(){
        return this.value;
    }

    get nextNode(){
        return this.next
    }

   public addNextNode(node:null|Node=null){
        this.next=node
    }
}

export default Node