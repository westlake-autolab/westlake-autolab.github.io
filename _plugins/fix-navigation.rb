# frozen_string_literal: true

module Jekyll
  module FixNavigationPlugin

    Jekyll::Hooks.register :site, :post_write do |site|
      # Only run for production builds (when building for deployment)
      next unless site.config['environment'] == 'production'

      Jekyll.logger.info "FixNavigation:", "Starting navigation link fixes after site generation..."
      
      total_fixes = 0
      dest_path = site.dest
      
      # Find all HTML files in the destination directory
      html_files = Dir.glob(File.join(dest_path, "**", "*.html"))
      Jekyll.logger.info "FixNavigation:", "Found #{html_files.length} HTML files"
      
      html_files.each do |file_path|
        relative_path = file_path.sub(dest_path, '')
        
        begin
          content = File.read(file_path, encoding: 'utf-8')
          original_content = content.dup
          
          # 1. Fix navigation links: /publications.html -> publications.html
          content.gsub!(/href="\/([^\/][^"]*\.html)"/, 'href="\1"')
          
          # 2. Fix root path links: href="/" -> href="index.html" (for non-index pages)
          unless relative_path.include?('index.html')
            content.gsub!(/href="\/"/, 'href="index.html"')
          end
          
          # 3. Fix canonical links: remove leading slash
          content.gsub!(/<link rel="canonical" href="\/([^"]*?)">/, '<link rel="canonical" href="\1">')
          
          # 4. Fix CSS links: /assets/css/style.css -> assets/css/style.css
          content.gsub!(/href="\/assets\/([^"]*)"/, 'href="assets/\1"')
          
          # 5. Fix JavaScript src: /assets/js/script.js -> assets/js/script.js
          content.gsub!(/src="\/assets\/([^"]*)"/, 'src="assets/\1"')
          
          # 6. Fix image src: /assets/img/image.jpg -> assets/img/image.jpg
          content.gsub!(/src="\/([^\/][^"]*)"/, 'src="\1"')
          
          # 7. Fix other asset references that might have been missed
          # This catches any remaining /path references that aren't external URLs
          content.gsub!(/="\/([^\/][^"]*)"/) do |match|
            path = $1
            # Skip if it looks like an external URL or already processed
            if path.start_with?('http') || path.start_with?('//')
              match
            else
              %Q{="#{path}"}
            end
          end
          
          # Write back if changed
          if content != original_content
            File.write(file_path, content, encoding: 'utf-8')
            total_fixes += 1
            Jekyll.logger.info "FixNavigation:", "✅ Fixed: #{relative_path}"
          else
            Jekyll.logger.info "FixNavigation:", "⏭️  No changes needed: #{relative_path}"
          end
          
        rescue => e
          Jekyll.logger.error "FixNavigation:", "Error processing #{relative_path}: #{e.message}"
        end
      end
      
      Jekyll.logger.info "FixNavigation:", "✨ Completed! Fixed #{total_fixes} files total"
    end
  end
end