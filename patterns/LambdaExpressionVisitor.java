package patterns;

import java.io.Writer;

import org.eclipse.jdt.core.dom.ITypeBinding;
import org.eclipse.jdt.core.dom.LambdaExpression;
import org.eclipse.jdt.core.dom.Type;

public class LambdaExpressionVisitor extends AbstractVisitor {
	
	public LambdaExpressionVisitor (Writer writer) {
		super(writer);
		System.out.println("(In LambdaVisitor) Debug line #: " +
                new Exception().getStackTrace()[0].getLineNumber());
	}
	

	
	@Override
    public boolean visit(LambdaExpression lambda)
    {
		System.out.println("- Lambda Visited, Debug Line #: " +
				new Exception().getStackTrace()[0].getLineNumber());
		
        int lineNumber = Unit.getLineNumber(lambda.getStartPosition()); // get the position of lambda expression
       
        String parent = GetEnclosingContainerName(lambda);
        if( parent != null ) // print the output to the file
        {
            
            WriteLine(lineNumber + ":" + parent);
            System.out.println(lineNumber + ":" + parent);
        }
        return true;
    }

}
