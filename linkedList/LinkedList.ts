

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

   public addNextNode(node:Node){
        this.next=node
    }
    
}

class LinkedList{
    tail?:Node
    constructor(initialVal?: any ){
          if (!!initialVal){
            this.tail=new Node(initialVal)
        }
     }

    public printList(){
        const list=[]
        let curr : null | undefined |  Node =this.tail
        do{
            list.push(curr?.nodeValue)
            curr=curr?.nextNode
        }while(!!curr)
        console.log(list.join(" -> "))
    }

    private getLastNode(){
        if(!this.tail)return null
        let lastNode =this.tail
        while(lastNode.nextNode){
            lastNode=lastNode.nextNode
        }
        return lastNode
    }

    public add(val:any){
        const lastNode =this.getLastNode()
        const newNode = new Node(val)
        if(lastNode){
            lastNode.addNextNode(newNode)
        }
        else{
            this.tail=newNode
        }
    }

    public reverse(){
        if(!this.tail)return null
        const nodes=[]
        let lastNode =this.tail
        while(lastNode.nextNode){
            nodes.push(lastNode)
            lastNode=lastNode.nextNode
        }
        nodes.push(lastNode)
        const reversedNodes = [...nodes].reverse()
         reversedNodes.forEach((node,i)=>node.addNextNode(reversedNodes?.[i+1]))
         this.tail=reversedNodes[0]
    }

    public remove(){}

}
export default LinkedList

const list  = new LinkedList("1")
list.add("2")
list.add("3")
list.add("4")
list.add("5")
list.printList()
list.reverse()
list.printList()
